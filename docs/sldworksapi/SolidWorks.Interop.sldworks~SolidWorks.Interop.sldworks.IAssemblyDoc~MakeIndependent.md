# MakeIndependent Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~MakeIndependent`

Makes the selected component independent.
Makes the selected component independent.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MakeIndependent( _
   ByVal FileName As System.String _
) As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim FileName As System.String
Dim value As System.Boolean
 
value = instance.MakeIndependent(FileName)
```

```

System.bool MakeIndependent( 
   System.string FileName
)
```

```

System.bool MakeIndependent( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   Path and file name where to save the new part (see **Remarks**)

#### Return Value

True if the component is made independent, false if not

Remarks

Making a component independent saves the component as a new file within the assembly and to the specified path and file name. The new part is referenced in the assembly.

Example

[Make Component Independent (C#)](Make_Component_Independent_Example_CSharp.htm)  
[Make Component Independent (VB.NET)](Make_Component_Independent_Example_VBNET.htm)  
[Make Component Independent (VBA)](Make_Component_Independent_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::ReplaceComponents2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReplaceComponents2.md)
