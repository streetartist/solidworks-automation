# GetRoot Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem~GetRoot`

Gets the root item of the FeatureManager design tree.
Gets the root item of the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRoot() As TreeControlItem
```

```

Dim instance As ITreeControlItem
Dim value As TreeControlItem
 
value = instance.GetRoot()
```

```

TreeControlItem GetRoot()
```

```

TreeControlItem^ GetRoot(); 
```

#### Return Value

[Root item of the FeatureManager design tree](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem.md)

Remarks

Use [ITreeControlItem::IsRoot](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem~IsRoot.md) to get whether an item is the root item of the FeatureManager design tree.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITreeControlItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem.md)  
[ITreeControlItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem_members.md)
