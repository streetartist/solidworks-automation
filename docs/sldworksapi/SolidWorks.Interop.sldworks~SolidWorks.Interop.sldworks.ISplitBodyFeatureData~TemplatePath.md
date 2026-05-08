# TemplatePath Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~TemplatePath`

Gets or sets the template to use to make this Split feature.
Gets or sets the template to use to make this Split feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TemplatePath As System.String
```

```

Dim instance As ISplitBodyFeatureData
Dim value As System.String
 
instance.TemplatePath = value
 
value = instance.TemplatePath
```

```

System.string TemplatePath {get; set;}
```

```

property System.String^ TemplatePath {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Path and file name of the template

Remarks

Set this property only if [ISplitBodyFeatureData::OverrideDefaultTemplateSettings](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~OverrideDefaultTemplateSettings.md) is set to true.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplitBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.md)  
[ISplitBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData_members.md)
