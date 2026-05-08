# GetSketchPoints Method (IWizardHoleFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~GetSketchPoints`

Gets the center-hole sketch points in this Hole Wizard feature.
Gets the center-hole sketch points in this Hole Wizard feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSketchPoints() As System.Object
```

```

Dim instance As IWizardHoleFeatureData2
Dim value As System.Object
 
value = instance.GetSketchPoints()
```

```

System.object GetSketchPoints()
```

```

System.Object^ GetSketchPoints(); 
```

#### Return Value

Array of center-hole [sketch points](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md)

Remarks

To add or remove sketch points in a Hole Wizard feature sketch (also called a location sketch), you must edit the sketch. After editing the sketch, update the Hole Wizard feature by calling [IModelDoc2::ForceRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.md).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

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
[IWizardHoleFeatureData2::GetSketchPointCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~GetSketchPointCount.md)  
[IWizardHoleFeatureData2::IGetSketchPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~IGetSketchPoints.md)
