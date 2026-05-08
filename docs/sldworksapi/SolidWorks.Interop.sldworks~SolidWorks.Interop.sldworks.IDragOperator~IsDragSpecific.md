# IsDragSpecific Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IsDragSpecific`

Gets or sets the drag-specific setting.
Gets or sets the drag-specific setting.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IsDragSpecific As System.Boolean
```

```

Dim instance As IDragOperator
Dim value As System.Boolean
 
instance.IsDragSpecific = value
 
value = instance.IsDragSpecific
```

```

System.bool IsDragSpecific {get; set;}
```

```

property System.bool IsDragSpecific {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True sets drag specific, false sets drag possible

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.md)  
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.md)
