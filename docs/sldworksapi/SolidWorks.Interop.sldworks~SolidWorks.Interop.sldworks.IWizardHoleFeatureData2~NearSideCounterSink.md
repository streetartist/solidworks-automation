# NearSideCounterSink Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~NearSideCounterSink`

Gets whether the near side option is selected for the Hole Wizard countersink feature.
Gets whether the near side option is selected for the Hole Wizard countersink feature.

****NOTE:** This property is a get-only property. Set is not implemented.**

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property NearSideCounterSink As System.Boolean
```

```

Dim instance As IWizardHoleFeatureData2
Dim value As System.Boolean
 
instance.NearSideCounterSink = value
 
value = instance.NearSideCounterSink
```

```

System.bool NearSideCounterSink {get; set;}
```

```

property System.bool NearSideCounterSink {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the near side option for the countersink Hole Wizard feature is selected, false if not (see **Remarks**)

Remarks

If you set this property to true, you must also set [IWizardHoleFeatureData2::NearCounterSinkDiameter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~NearCounterSinkDiameter.md) to an appropriate value in meters and [IWizardHoleFeatureData2::NearCounterSinkAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~NearCounterSinkAngle.md) to an appropriate value in radians to modify the Hole Wizard feature definition. If you do not set the diameter and angle to their proper values, then this method has no effect.

Example

[Select Near and Far Side Hole Wizard Countersink Options (C#)](Select_Near_and_Far_Side_Countersink_Hole_Options_Example_CSharp.htm)  
[Select Near and Far Side Hole Wizard Countersink Options (VB.NET)](Select_Near_and_Far_Side_Countersink_Hole_Options_Example_VBNET.htm)  
[Select Near and Far Side Hole Wizard Countersink Options (VBA)](Select_Near_and_Far_Side_Countersink_Hole_Options_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.md)  
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.md)  
[IWizardHoleFeatureData2::FarSideCounterSink Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FarSideCounterSink.md)  
[IWizardHoleFeatureData2::FarCounterSinkAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FarCounterSinkAngle.md)  
[IWizardHoleFeatureData2::FarCounterSinkDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FarCounterSinkDiameter.md)  
[IWizardHoleFeatureData2::CounterSinkAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~CounterSinkAngle.md)  
[IWizardHoleFeatureData2::CounterSinkDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~CounterSinkDiameter.md)  
[IWizardHoleFeatureData2::MidCounterSinkAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~MidCounterSinkAngle.md)  
[IWizardHoleFeatureData2::MidCounterSinkDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~MidCounterSinkDiameter.md)
