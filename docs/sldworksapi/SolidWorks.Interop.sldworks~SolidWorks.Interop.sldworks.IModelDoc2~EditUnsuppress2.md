# EditUnsuppress2 Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditUnsuppress2`

Unsuppresses the selected feature or component.
Unsuppresses the selected feature or component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EditUnsuppress2() As System.Boolean
```

```

Dim instance As IModelDoc2
Dim value As System.Boolean
 
value = instance.EditUnsuppress2()
```

```

System.bool EditUnsuppress2()
```

```

System.bool EditUnsuppress2(); 
```

#### Return Value

True if the selected feature or component is unsuppressed, false if not

Remarks

This routine is identical to the obsoleted IModelDoc2::EditUnsuppress. The version number was incremented to allow VB applications to take advantage of information not available in the obsoleted IPartDoc::EditUnsuppress.

Example

[Set and Get Sheet Metal Part's Persistent Reference IDs (C#)](Set_and_Get_Sheet_Metal_Part's_Persistent_Reference_IDs_Example_CSharp.htm)  
[Set and Get Sheet Metal Part's Persistent Reference IDs (VB.NET)](Set_and_Get_Sheet_Metal_Part's_Persistent_Reference_IDs_Example_VBNET.htm)  
[Set and Get Sheet Metal Part's Persistent Reference IDs (VBA)](Set_and_Get_Sheet_Metal_Part's_Persistent_Reference_IDs_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::EditSuppress2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditSuppress2.md)  
[IModelDoc2::EditUnsuppressDependent2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditUnsuppressDependent2.md)
