# IEnumDocuments2 Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments2`

Allows access to a documents enumeration.
Allows access to a [documents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) enumeration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IEnumDocuments2 
```

```

Dim instance As IEnumDocuments2
```

```

public interface IEnumDocuments2 
```

```

public interface class IEnumDocuments2 
```

Remarks

For use in in-process DLLs only.

The list of [IModelDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) objects in the IEnumDocuments2 object contains all open IModelDoc2 pointers, including IModelDoc2 objects opened as file references (for example, from an assembly or drawing). You can use [IModelDoc2::Visible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Visible.md) to determine if a particular document has its own window and is visible to the user.

Example

[Get List of Open Documents (C++)](Get_List_of_Open_Documents_Example_CPlusPlus_COM.htm)  
[Traverse All Open Documents (C++)](Traverse_All_Open_Documents_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnumDocuments2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments2_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
