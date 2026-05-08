# Attach3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~Attach3`

Activates the BOM.
Activates the BOM.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Attach3() As System.Boolean
```

```

Dim instance As IBomTable
Dim value As System.Boolean
 
value = instance.Attach3()
```

```

System.bool Attach3()
```

```

System.bool Attach3(); 
```

#### Return Value

True if successfully attached, false if not

Remarks

If you want SOLIDWORKS to run in the background, then do not use this method. Using this method will cause SOLIDWORKS to become visible.

You must call this method before using any of the [IBomTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable.md) methods.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable.md)  
[IBomTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable_members.md)  
[IBomTable::Detach](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~Detach.md)
