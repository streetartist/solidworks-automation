# IsRoot Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem~IsRoot`

Gets whether this item is the root item of the FeatureManager design tree.
Gets whether this item is the root item of the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property IsRoot As System.Boolean
```

```

Dim instance As ITreeControlItem
Dim value As System.Boolean
 
value = instance.IsRoot
```

```

System.bool IsRoot {get;}
```

```

property System.bool IsRoot {
   System.bool get();
}
```

#### Property Value

True if this item is the root item of the FeatureManager design tree, false if not

Remarks

Use [ITreeControlItem::GetRoot](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem~GetRoot.md) to get the root item of the FeatureManager design tree.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITreeControlItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem.md)  
[ITreeControlItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem_members.md)
