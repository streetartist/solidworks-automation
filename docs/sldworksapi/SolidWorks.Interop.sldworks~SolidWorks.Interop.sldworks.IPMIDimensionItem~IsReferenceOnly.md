# IsReferenceOnly Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~IsReferenceOnly`

Gets whether this PMI dimension is reference only.
Gets whether this PMI dimension is reference only.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsReferenceOnly() As System.Boolean
```

```

Dim instance As IPMIDimensionItem
Dim value As System.Boolean
 
value = instance.IsReferenceOnly()
```

```

System.bool IsReferenceOnly()
```

```

System.bool IsReferenceOnly(); 
```

#### Return Value

True if this PMI dimension is reference-only, false if not

Remarks

If this method returns true, then this dimension item is used for information purposes only. It does not govern production or inspection operations.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPMIDimensionItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem.md)  
[IPMIDimensionItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem_members.md)
