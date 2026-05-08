# ChangeStandard Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ChangeStandard`

Sets the standard for all of the parameters of the Hole Wizard feature that are driven by the database.
Sets the standard for all of the parameters of the Hole Wizard feature that are driven by the database.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ChangeStandard( _
   ByVal Standard As System.Integer, _
   ByVal FastenerType As System.Integer, _
   ByVal SSize As System.String _
) As System.Boolean
```

```

Dim instance As IWizardHoleFeatureData2
Dim Standard As System.Integer
Dim FastenerType As System.Integer
Dim SSize As System.String
Dim value As System.Boolean
 
value = instance.ChangeStandard(Standard, FastenerType, SSize)
```

```

System.bool ChangeStandard( 
   System.int Standard,
   System.int FastenerType,
   System.string SSize
)
```

```

System.bool ChangeStandard( 
   System.int Standard,
   System.int FastenerType,
   System.String^ SSize
) 
```

#### Parameters

*Standard*
:   Standard as defined in [swWzdHoleStandards\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleStandards_e.html)

*FastenerType*
:   Fastener type as defined in [swWzdHoleStandardFastenerTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleStandardFastenerTypes_e.html)

*SSize*
:   Fastener size

#### Return Value

True if the standard is changed, false if not

Remarks

Use this method to change [fastener size](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FastenerSize.md), [fastener type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FastenerType2.md), and [design standard](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~Standard2.md) of a Hole Wizard feature.

If changing the standard requires you to change the type, then you must call [IWizardHoleFeatureData2::Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~Type.md) before calling IWizardHoleFeatureData2::ChangeStandard.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.md)  
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.md)
