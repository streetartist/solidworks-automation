# IncludeEnvelopeComponents Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData~IncludeEnvelopeComponents`

Gets or sets whether to include envelope components in this bounding box feature.
Gets or sets whether to include envelope components in this bounding box feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IncludeEnvelopeComponents As System.Boolean
```

```

Dim instance As IBoundingBoxFeatureData
Dim value As System.Boolean
 
instance.IncludeEnvelopeComponents = value
 
value = instance.IncludeEnvelopeComponents
```

```

System.bool IncludeEnvelopeComponents {get; set;}
```

```

property System.bool IncludeEnvelopeComponents {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to include envelope components, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBoundingBoxFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData.md)  
[IBoundingBoxFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData_members.md)
