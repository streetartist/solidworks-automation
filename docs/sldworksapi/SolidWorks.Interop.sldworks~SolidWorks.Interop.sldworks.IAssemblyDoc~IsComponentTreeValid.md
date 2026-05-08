# IsComponentTreeValid Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IsComponentTreeValid`

Checks the validity of the component tree for this assembly.
Checks the validity of the component tree for this assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsComponentTreeValid() As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim value As System.Boolean
 
value = instance.IsComponentTreeValid()
```

```

System.bool IsComponentTreeValid()
```

```

System.bool IsComponentTreeValid(); 
```

#### Return Value

True if the component tree is currently valid, false if the tree is currently invalid

Remarks

In certain cases, the current assembly component tree is invalid.

- You cannot query the assembly for a list of components [(IComponent2::GetChildren](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetChildren.md)) or use existing IComponent2 objects to make function calls.
- If you use the IComponent2 object's methods, then this method returns a NULL or empty value.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)
