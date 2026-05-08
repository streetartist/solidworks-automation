# AssemblyFeatureScope Property (IWizardHoleFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~AssemblyFeatureScope`

Gets or sets whether to use scope for this assembly Hole Wizard feature.
Gets or sets whether to use scope for this assembly Hole Wizard feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AssemblyFeatureScope As System.Boolean
```

```

Dim instance As IWizardHoleFeatureData2
Dim value As System.Boolean
 
instance.AssemblyFeatureScope = value
 
value = instance.AssemblyFeatureScope
```

```

System.bool AssemblyFeatureScope {get; set;}
```

```

property System.bool AssemblyFeatureScope {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use feature scope, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.md)  
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.md)  
[IWizardHoleFeatureData2::AutoSelect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~AutoSelect.md)  
[IWizardHoleFeatureData2::AutoSelectComponents Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~AutoSelectComponents.md)  
[IWizardHoleFeatureData2::PropagateFeatureToParts Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~PropagateFeatureToParts.md)
