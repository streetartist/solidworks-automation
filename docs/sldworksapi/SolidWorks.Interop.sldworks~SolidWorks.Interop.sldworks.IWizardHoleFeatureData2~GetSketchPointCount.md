# GetSketchPointCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~GetSketchPointCount`

Gets the number of center-hole sketch points in this Hole Wizard feature.
Gets the number of center-hole sketch points in this Hole Wizard feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSketchPointCount() As System.Integer
```

```

Dim instance As IWizardHoleFeatureData2
Dim value As System.Integer
 
value = instance.GetSketchPointCount()
```

```

System.int GetSketchPointCount()
```

```

System.int GetSketchPointCount(); 
```

#### Return Value

Number of center-hole sketch points

Remarks

Call this method before calling [IWizardHoleFeatureData2::IGetSketchPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~IGetSketchPoints.md).

Example

[Get and Add Sketch Points in Hole Wizard Feature (C#)](Get_Sketch_Points_in_Wizard_Hole_Example_CSharp.htm)  
[Get and Add Sketch Points in Hole Wizard Feature (VB.NET)](Get_Sketch_Points_in_Wizard_Hole_Example_VBNET.htm)  
[Get and Add Sketch Points in Hole Wizard Feature (VBA)](Get_Sketch_Points_in_Wizard_Hole_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.md)  
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.md)  
[IWizardHoleFeatureData2::GetSketchPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~GetSketchPoints.md)
