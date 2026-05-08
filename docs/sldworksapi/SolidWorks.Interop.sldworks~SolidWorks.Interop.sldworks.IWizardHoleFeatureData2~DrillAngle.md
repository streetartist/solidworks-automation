# DrillAngle Property (IWizardHoleFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~DrillAngle`

Gets or sets the drill angle for a Hole Wizard feature.
Gets or sets the drill angle for a Hole Wizard feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DrillAngle As System.Double
```

```

Dim instance As IWizardHoleFeatureData2
Dim value As System.Double
 
instance.DrillAngle = value
 
value = instance.DrillAngle
```

```

System.double DrillAngle {get; set;}
```

```

property System.double DrillAngle {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Drill angle

Remarks

This property is relevant only for swSimpleDrilled, swTaperedDrilled, swCounterBoreDrilled, swCounterSunkDrilled, and swCounterDrilledDrilled holes.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See **Create Holes Using Hole Wizard and Sketch Points** examples in [IWizardHoleFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.md)  
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.md)  
[IWizardHoleFeaturData2::CounterDrillAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~CounterDrillAngle.md)  
[IWizardHoleFeaturData2::CounterDrillDepth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~CounterDrillDepth.md)  
[IWizardHoleFeaturData2::CounterDrillDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~CounterDrillDiameter.md)
