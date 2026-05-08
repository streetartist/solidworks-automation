# InsertProjectedSketch2 Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertProjectedSketch2`

Obsolete. See IProjectionCurveFeatureData and IFeatureManager::CreateDefinition.
Obsolete. See [IProjectionCurveFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData.md) and [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertProjectedSketch2( _
   ByVal Reverse As System.Integer _
) As System.Object
```

```

Dim instance As IModelDoc2
Dim Reverse As System.Integer
Dim value As System.Object
 
value = instance.InsertProjectedSketch2(Reverse)
```

```

System.object InsertProjectedSketch2( 
   System.int Reverse
)
```

```

System.Object^ InsertProjectedSketch2( 
   System.int Reverse
) 
```

#### Parameters

*Reverse*
:   1 to reverse the projected direction, 0 to not reverse the projected direction

#### Return Value

Newly created [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) or Nothing or null if the operation fails

Remarks

You can reverse the direction in which the curve is projected. This is necessary only when the selected face wraps around the plane of the curve. For example, if the sketch being projected is surrounded by a cylindrical face, then two possible projections exist. The reverse argument switches the direction based on the normal vector of the sketch. The default direction is along the sketch normal.

Example

[Get Projected Curve Feature Data (C#)](Get_Projected_Curve_Feature_Data_Example_CSharp.htm)  
[Get Projected Curve Feature Data (VB.NET)](Get_Projected_Curve_Feature_Data_Example_VBNET.htm)  
[Get Projected Curve Feature Data (VBA)](Get_Projected_Curve_Feature_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::IInsertProjectedSketch2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IInsertProjectedSketch2.md)
