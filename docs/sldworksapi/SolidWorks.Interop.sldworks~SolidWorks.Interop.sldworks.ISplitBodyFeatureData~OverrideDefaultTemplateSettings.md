# OverrideDefaultTemplateSettings Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~OverrideDefaultTemplateSettings`

Gets or sets whether to use an alternate template to apply to all new part or assembly files created during the split operation.
Gets or sets whether to use an alternate template to apply to all new part or assembly files created during the split operation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property OverrideDefaultTemplateSettings As System.Boolean
```

```

Dim instance As ISplitBodyFeatureData
Dim value As System.Boolean
 
instance.OverrideDefaultTemplateSettings = value
 
value = instance.OverrideDefaultTemplateSettings
```

```

System.bool OverrideDefaultTemplateSettings {get; set;}
```

```

property System.bool OverrideDefaultTemplateSettings {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use an alternate template, false to use the default template

Remarks

Use [ISplitBodyFeatureData::TemplatePath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~TemplatePath.md) to specify the alternate template.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplitBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.md)  
[ISplitBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData_members.md)
