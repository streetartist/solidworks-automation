# GetPrevious Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem~GetPrevious`

Gets the previous sibling of this item in the FeatureManager design tree.
Gets the previous sibling of this item in the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPrevious() As TreeControlItem
```

```

Dim instance As ITreeControlItem
Dim value As TreeControlItem
 
value = instance.GetPrevious()
```

```

TreeControlItem GetPrevious()
```

```

TreeControlItem^ GetPrevious(); 
```

#### Return Value

[Previous sibling of this item in the FeatureManager design tree](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem~GetPrevious.md)

Remarks

Use [ITreeControlItem::GetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem~GetNext.md) to get the next sibling of this item in the FeatureManager design tree.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITreeControlItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem.md)  
[ITreeControlItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem_members.md)
