# ExcludeFromCutList Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ExcludeFromCutList`

Gets or sets whether to exclude this feature from the cut list.
Gets or sets whether to exclude this feature from the cut list.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ExcludeFromCutList As System.Boolean
```

```

Dim instance As IFeature
Dim value As System.Boolean
 
instance.ExcludeFromCutList = value
 
value = instance.ExcludeFromCutList
```

```

System.bool ExcludeFromCutList {get; set;}
```

```

property System.bool ExcludeFromCutList {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to exclude, false to not

Remarks

This method only works for cut list items.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)
