# EditSuppress2 Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditSuppress2`

Suppresses the selected feature, the selected component, or the owning feature of the selected face.
Suppresses the selected feature, the selected component, or the owning feature of the selected face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EditSuppress2() As System.Boolean
```

```

Dim instance As IModelDoc2
Dim value As System.Boolean
 
value = instance.EditSuppress2()
```

```

System.bool EditSuppress2()
```

```

System.bool EditSuppress2(); 
```

#### Return Value

True if the selected feature, component, or owning feature of the selected face is suppressed, false if not

Remarks

This routine is identical to the now obsolete IModelDoc2::EditSuppress. The version number was incremented to allow VB applications to take advantage of information not available in the now obsolete IPartDoc::EditSuppress2.

This method closes any component files when called in an assembly. If the components were modified, then those modifications are not automatically saved. You must save any modifications before the files are closed.

SOLIDWORKS does not allow suppressing features or components while a PropertyManager page is open.

Example

[Suppress Feature (VBA)](Suppress_Feature_Example_VB.htm)  
[Set and Get Sheet Metal Part's Persistent Reference IDs (C#)](Set_and_Get_Sheet_Metal_Part's_Persistent_Reference_IDs_Example_CSharp.htm)  
[Set and Get Sheet Metal Part's Persistent Reference IDs (VB.NET)](Set_and_Get_Sheet_Metal_Part's_Persistent_Reference_IDs_Example_VBNET.htm)  
[Set and Get Sheet Metal Part's Persistent Reference IDs (VBA)](Set_and_Get_Sheet_Metal_Part's_Persistent_Reference_IDs_Example_VB.htm)  
[Suppress Component Feature (C#)](Suppress_Component_Feature_Example_CSharp.htm)  
[Suppress Component Feature (VB.NET)](Suppress_Component_Feature_Example_VBNET.htm)  
[Suppress Component Feature (VBA)](Suppress_Component_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::EditUnsuppress2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditUnsuppress2.md)  
[IModelDoc2::EditUnsuppressDependent2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditUnsuppressDependent2.md)
