# AutoPropagation Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~AutoPropagation`

Gets or sets whether to automatically add tangent faces to the cut-extrude face group.
Gets or sets whether to automatically add tangent faces to the cut-extrude face group.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AutoPropagation As System.Boolean
```

```

Dim instance As ISMNormalCutFeatureData2
Dim value As System.Boolean
 
instance.AutoPropagation = value
 
value = instance.AutoPropagation
```

```

System.bool AutoPropagation {get; set;}
```

```

property System.bool AutoPropagation {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to add tangent faces, false to not

Example

See the [ISMNormalCutFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMNormalCutFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.md)  
[ISMNormalCutFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2_members.md)
