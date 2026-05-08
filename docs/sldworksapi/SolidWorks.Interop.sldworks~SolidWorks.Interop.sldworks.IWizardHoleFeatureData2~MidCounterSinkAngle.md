# MidCounterSinkAngle Property (IWizardHoleFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~MidCounterSinkAngle`

Gets or sets the angle of the Hole Wizard middle countersink feature.
Gets or sets the angle of the Hole Wizard middle countersink feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MidCounterSinkAngle As System.Double
```

```

Dim instance As IWizardHoleFeatureData2
Dim value As System.Double
 
instance.MidCounterSinkAngle = value
 
value = instance.MidCounterSinkAngle
```

```

System.double MidCounterSinkAngle {get; set;}
```

```

property System.double MidCounterSinkAngle {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Middle countersink angle

Remarks

This property is relevant only for swCounterSunk and swCounterSunkDrilled holes.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

[Create Holes Using Hole Wizard and Sketch Points (VBA)](Create_Holes_using_Hole_Wizard_and_Sketch_Points_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.md)  
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.md)  
[IWizardHoleFeatureData2::CounterSinkAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~CounterSinkAngle.md)  
[IWizardHoleFeatureData2::CounterSinkDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~CounterSinkDiameter.md)  
[IWizardHoleFeatureData2::FarCounterSinkAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FarCounterSinkAngle.md)  
[IWizardHoleFeatureData2::FarCounterSinkDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FarCounterSinkDiameter.md)  
[IWizardHoleFeatureData2::MidCounterSinkDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~MidCounterSinkDiameter.md)  
[IWizardHoleFeatureData2::NearCounterSinkAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~NearCounterSinkAngle.md)  
[IWizardHoleFeatureData2::NearCounterSinkDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~NearCounterSinkDiameter.md)  
[IWizardHoleFeatureData2::NearSideCounterSink Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~NearSideCounterSink.md)  
[IWizardHoleFeatureData2::FarSideCounterSink Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FarSideCounterSink.md)
