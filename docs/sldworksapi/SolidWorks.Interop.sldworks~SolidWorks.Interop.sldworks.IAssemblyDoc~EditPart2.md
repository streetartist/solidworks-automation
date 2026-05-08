# EditPart2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditPart2`

Edits the selected part within the context of an assembly.
Edits the selected part within the context of an assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EditPart2( _
   ByVal Silent As System.Boolean, _
   ByVal AllowReadOnly As System.Boolean, _
   ByRef Information As System.Integer _
) As System.Integer
```

```

Dim instance As IAssemblyDoc
Dim Silent As System.Boolean
Dim AllowReadOnly As System.Boolean
Dim Information As System.Integer
Dim value As System.Integer
 
value = instance.EditPart2(Silent, AllowReadOnly, Information)
```

```

System.int EditPart2( 
   System.bool Silent,
   System.bool AllowReadOnly,
   ref System.int Information
)
```

```

System.int EditPart2( 
   System.bool Silent,
   System.bool AllowReadOnly,
   System.int% Information
) 
```

#### Parameters

*Silent*
:   True to suppress messages to user, false to not

*AllowReadOnly*
:   True to allow editing of read-only parts, false to not

*Information*
:   Status as defined in [swEditPartCommandStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEditPartCommandStatus_e.html)

#### Return Value

swEditPartSuccessful if successful

Remarks

This method allows you to control the display of dialog boxes and edit a read-only document. To return to editing the assembly, use [IAssemblyDoc::EditAssembly](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditAssembly.md).

Example

[Create Plane thru 3 Points In-context (VBA)](Create_Plane_Thru_3_Points_In-context_Example_VB.htm)  
[Suppress Component Feature (C#)](Suppress_Component_Feature_Example_CSharp.htm)  
[Suppress Component Feature (VB.NET)](Suppress_Component_Feature_Example_VBNET.htm)  
[Suppress Component Feature (VBA)](Suppress_Component_Feature_Example_VB.htm)  
[Insert Cavity (C#)](Insert_Cavity_Example_CSharp.htm)  
[Insert Cavity (VB.NET)](Insert_Cavity_Example_VBNET.htm)  
[Insert Cavity (VBA)](Insert_Cavity_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)
