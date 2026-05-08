# ReverseTranslationDirection Property (IPartExplodeStep)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep~ReverseTranslationDirection`

Gets or sets whether to reverse the direction of explode in this explode step.
Gets or sets whether to reverse the direction of explode in this explode step.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReverseTranslationDirection As System.Boolean
```

```

Dim instance As IPartExplodeStep
Dim value As System.Boolean
 
instance.ReverseTranslationDirection = value
 
value = instance.ReverseTranslationDirection
```

```

System.bool ReverseTranslationDirection {get; set;}
```

```

property System.bool ReverseTranslationDirection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to reverse the direction of explode, false to not

Example

See the [IPartExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.md)  
[IPartExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep_members.md)
