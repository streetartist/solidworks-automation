# IUserUnit Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit`

Allows you to manage units.
Allows you to manage units.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IUserUnit 
```

```

Dim instance As IUserUnit
```

```

public interface IUserUnit 
```

```

public interface class IUserUnit 
```

Remarks

| If you obtain IUserUnit using... | Then IUserUnit's properties are... |
| --- | --- |
| [IModelDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) | Read only and persistent. Use IModelDocExtension::SetUserPreference\* methods to set the units properties of a document. |
| [ISldWorks](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md) | Read-write, but not persistent. The instance of IUserUnit returned by ISldWorks is empty and not tied to any document. Use this instance as a template to store units properties at runtime. |

**NOTE**: Use this interface instead of **mo\_UserUnits.h** file in *public\_documents***\appcomm** of your SOLIDWORKS installation. If you previously used **mo\_UserUnits.h**, you should change your applications to use this interface.

Example

[Get and Set Document Units (VBA)](Get_and_Set_User_Units_Example_VB.htm)  
[Get and Set Document Units (VB.NET)](Get_and_Set_User_Units_Example_VBNET.htm)  
[Get and Set Document Units (C#)](Get_and_Set_User_Units_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IUserUnit Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
