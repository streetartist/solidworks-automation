# EditUnsuppressDependent2 Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditUnsuppressDependent2`

Unsuppresses the selected feature or component and their dependents.
Unsuppresses the selected feature or component and their dependents.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EditUnsuppressDependent2() As System.Boolean
```

```

Dim instance As IModelDoc2
Dim value As System.Boolean
 
value = instance.EditUnsuppressDependent2()
```

```

System.bool EditUnsuppressDependent2()
```

```

System.bool EditUnsuppressDependent2(); 
```

#### Return Value

True if the selected feature or component and their dependents are unsuppressed, false if not

Remarks

This method is identical to the obsoleted IModelDoc2::EditUnsuppressDependent method. The version number was incremented to allow Visual Basic applications to take advantage of information not available in the obsoleted IPartDoc::EditUnsuppressDependent method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::EditSuppress2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditSuppress2.md)  
[IModelDoc2::EditUnsuppress2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditUnsuppress2.md)
