# InsertMidSurfaceExt Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertMidSurfaceExt`

Obsolete. Superseded by IFeatureManager::InsertMidSurface.
Obsolete. Superseded by [IFeatureManager::InsertMidSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMidSurface.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertMidSurfaceExt( _
   ByVal Placement As System.Double, _
   ByVal KnitFlag As System.Boolean _
) As System.Object
```

```

Dim instance As IModelDoc2
Dim Placement As System.Double
Dim KnitFlag As System.Boolean
Dim value As System.Object
 
value = instance.InsertMidSurfaceExt(Placement, KnitFlag)
```

```

System.object InsertMidSurfaceExt( 
   System.double Placement,
   System.bool KnitFlag
)
```

```

System.Object^ InsertMidSurfaceExt( 
   System.double Placement,
   System.bool KnitFlag
) 
```

#### Parameters

*Placement*
:   Value from -1 to 1 that indicates the desired location of the midsurface relative to the face pair; a value of 0.0 places the midsurface equally between the face pair

*KnitFlag*
:   True to sew all the reference surfaces (neutral sheets) into a single sheet(surface) body, false for the midsurface feature to contain individual reference surface geometry

#### Return Value

[Mid-surface feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2.md)

Remarks

A midsurface feature is calculated from the solid body in your part document. This method first finds all parallel pairs of faces from the part solid. For each pair of parallel faces found, it creates a neutral reference surface between the two faces. The placement position of the reference surface is controlled by the placement parameter. This process repeats itself until all parallel body faces are processed. At the end of this process, all the reference surfaces are sewn into a single reference surface if knitFlag is set to True.

The hierarchy of a midsurface feature is:

A midsurface feature contains one or more reference surfaces. If sewn successfully using the knitFlag = True option, then the midsurface feature contains only one reference surface. Each reference surface is considered a sheet body. The sheet body has the normal topology that you would expect to find on a body object (for example, faces, edges, and so on). See the [IMidSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2.md) object for methods that provide access to this topology.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::IInsertMidSurfaceExt Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IInsertMidSurfaceExt.md)
