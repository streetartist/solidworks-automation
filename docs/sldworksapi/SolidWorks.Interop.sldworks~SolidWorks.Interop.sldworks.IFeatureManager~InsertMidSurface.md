# InsertMidSurface Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMidSurface`

Inserts a midsurface feature.
Inserts a midsurface feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertMidSurface( _
   ByVal PBodyIn As Body2, _
   ByVal PPartDocIn As ModelDoc2, _
   ByVal Placement As System.Double, _
   ByVal KnitFlag As System.Boolean _
) As System.Object
```

```

Dim instance As IFeatureManager
Dim PBodyIn As Body2
Dim PPartDocIn As ModelDoc2
Dim Placement As System.Double
Dim KnitFlag As System.Boolean
Dim value As System.Object
 
value = instance.InsertMidSurface(PBodyIn, PPartDocIn, Placement, KnitFlag)
```

```

System.object InsertMidSurface( 
   Body2 PBodyIn,
   ModelDoc2 PPartDocIn,
   System.double Placement,
   System.bool KnitFlag
)
```

```

System.Object^ InsertMidSurface( 
   Body2^ PBodyIn,
   ModelDoc2^ PPartDocIn,
   System.double Placement,
   System.bool KnitFlag
) 
```

#### Parameters

*PBodyIn*
:   [Body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) in the context of an assembly; otherwise, null or Nothing (see **Remarks**)

*PPartDocIn*
:   [Model document](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) in the context of an assembly; otherwise, null or Nothing (see **Remarks**)

*Placement*
:   Value from -1 to 1 that indicates the desired location of the midsurface relative to the face pair; a value of 0.0 places the midsurface equally between the face pair

*KnitFlag*
:   True to sew all the reference surfaces (neutral sheets) into a single sheet (surface) body, false for the midsurface feature to contain individual reference surface geometry

#### Return Value

Newly created [midsurface feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3.md)

Remarks

The pPartDocIn parameter is the component's model document where you want to add the midsurface feature, and the pBody parameter is the body of that component.

A midsurface feature is calculated from the solid body in your part document. This method first finds all parallel pairs of faces from the part solid. For each pair of parallel faces found, it creates a neutral reference surface between the two faces. The placement position of the reference surface is controlled by the placement parameter. This process repeats itself until all parallel body faces are processed. At the end of this process, all the reference surfaces are sewn into a single reference surface if knitFlag is set to true.

The hierarchy of a midsurface feature is a midsurface feature contains one or more reference surfaces. If sewn successfully using the KnitFlag = True option, then the midsurface feature contains only one reference surface. Each reference surface is considered a sheet body. The sheet body has the normal topology that you would expect to find on a body object (for example, faces, edges, and so on). See [IMidSurface3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3.md) for methods that provide access to this topology.

Example

[Insert MidSurface in Component (C#)](Insert_MidSurface_in_Component_Example_CSharp.htm)  
[Insert MidSurface in Component (VB.NET)](Insert_MidSurface_in_Component_Example_VBNET.htm)  
[Insert MidSurface in Component (VBA)](Insert_MidSurface_in_Component_Example_VB.htm)  
[Get Areas of Midsurface Faces (C#)](Get_Areas_of_MidSurface_Faces_Example_CSharp.htm)  
[Get Areas of Midsurface Faces (VB.NET)](Get_Areas_of_MidSurface_FAces_Example_VBNET.htm)  
[Get Areas of Midsurface Faces (VBA)](Get_Areas_of_MidSurface_Faces_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
