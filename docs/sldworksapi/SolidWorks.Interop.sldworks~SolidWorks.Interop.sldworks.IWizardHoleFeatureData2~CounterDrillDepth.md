# CounterDrillDepth Property (IWizardHoleFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~CounterDrillDepth`

Gets or sets the Hole Wizard feature counterdrill depth.
Gets or sets the Hole Wizard feature counterdrill depth.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CounterDrillDepth As System.Double
```

```

Dim instance As IWizardHoleFeatureData2
Dim value As System.Double
 
instance.CounterDrillDepth = value
 
value = instance.CounterDrillDepth
```

```

System.double CounterDrillDepth {get; set;}
```

```

property System.double CounterDrillDepth {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Counterdrill depth

Remarks

This property is relevant only for swCounterDrilled and swCounterDrilledDrilled holes.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See **Create Holes Using Hole Wizard and Sketch Points** examples in [IWizardHoleFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.md)  
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.md)  
[IWizardHoleFeatureData2::CounterDrillAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~CounterDrillAngle.md)  
[IWizardHoleFeatureData2::CounterDrillDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~CounterDrillDiameter.md)  
[IWizardHoleFeaturData2::DrillAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~DrillAngle.md)
