# Length Property (IWizardHoleFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~Length`

Gets or sets the length of a Hole Wizard slot feature.
Gets or sets the length of a Hole Wizard slot feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Length As System.Double
```

```

Dim instance As IWizardHoleFeatureData2
Dim value As System.Double
 
instance.Length = value
 
value = instance.Length
```

```

System.double Length {get; set;}
```

```

property System.double Length {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Length of slot

Remarks

This property is only valid for slots.

Example

[Insert Hole Wizard Slot and Hole (C#)](Insert_Hole_Wizard_Slot_and_Hole_Example_CSharp.htm)  
[Insert Hole Wizard Slot and Hole (VB.NET)](Insert_Hole_Wizard_Slot_and_Hole_Example_VBNET.htm)  
[Insert Hole Wizard Slot and Hole (VBA)](Insert_Hole_Wizard_Slot_and_Hole_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.md)  
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.md)
