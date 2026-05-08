# IsWeldment Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IsWeldment`

Gets whether this part contains a weldment feature.
Gets whether this part contains a weldment feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsWeldment() As System.Boolean
```

```

Dim instance As IPartDoc
Dim value As System.Boolean
 
value = instance.IsWeldment()
```

```

System.bool IsWeldment()
```

```

System.bool IsWeldment(); 
```

#### Return Value

True if part contains a weldment feature, false if not

Example

[Does Part Contain a Weldment Feature (VBA)](Does_Part_Contain_a_Weldment_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)
