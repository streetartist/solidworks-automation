# MakeAssemblyFromSelectedComponents Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~MakeAssemblyFromSelectedComponents`

Creates a new assembly comprised of the selected components of this assembly.
Creates a new assembly comprised of the selected components of this assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MakeAssemblyFromSelectedComponents( _
   ByVal FileName As System.String _
) As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim FileName As System.String
Dim value As System.Boolean
 
value = instance.MakeAssemblyFromSelectedComponents(FileName)
```

```

System.bool MakeAssemblyFromSelectedComponents( 
   System.string FileName
)
```

```

System.bool MakeAssemblyFromSelectedComponents( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   Path and filename of the new assembly

#### Return Value

True if a new assembly is created, false if not

Remarks

If **Tools > Options > System Options > Assemblies >  Save new components to external files** is selected, then a virtual sub-assembly is created and saved to an external file. Be sure to save the parent assembly before calling this method.

If **Tools > Options > System Options > Assemblies >  Save new components to external files** is not selected, then the *FileName* input parameter is ignored, and only a virtual sub-assembly is created.

Example

[Make Assembly From Selected Components (VB.NET)](Make_Assembly_From_Selected_Components_Example_VBNET.htm)  
[Make Assembly From Selected Components (VBA)](Make_Assembly_From_Selected_Components_Example_VB.htm)  
[Make Assembly From Selected Components (C#)](Make_Assembly_From_Selected_Components_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)
