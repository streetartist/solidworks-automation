# HeadClearanceType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~HeadClearanceType`

Gets the type of head clearance for this countersink Hole Wizard feature.
Gets the type of head clearance for this countersink Hole Wizard feature.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property HeadClearanceType As System.Integer
```

```

Dim instance As IWizardHoleFeatureData2
Dim value As System.Integer
 
instance.HeadClearanceType = value
 
value = instance.HeadClearanceType
```

```

System.int HeadClearanceType {get; set;}
```

```

property System.int HeadClearanceType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of head clearance as defined in [swWzdHoleCounterSinkHeadClearanceTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleCounterSinkHeadClearanceTypes_e.html)

Example

See **Create Holes Using Hole Wizard and Sketch Points** examples in [IWizardHoleFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.md)  
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.md)  
[IWizardHoleFeatureData2::HeadClearance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~HeadClearance.md)
