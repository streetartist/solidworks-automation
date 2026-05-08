# AddPipingFitting Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddPipingFitting`

Adds a pipe fitting to the current piping assembly.
Adds a pipe fitting to the current piping assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddPipingFitting( _
   ByVal PathName As System.String, _
   ByVal ConfigName As System.String, _
   ByVal AlignmentIndex As System.Short _
) As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim PathName As System.String
Dim ConfigName As System.String
Dim AlignmentIndex As System.Short
Dim value As System.Boolean
 
value = instance.AddPipingFitting(PathName, ConfigName, AlignmentIndex)
```

```

System.bool AddPipingFitting( 
   System.string PathName,
   System.string ConfigName,
   System.short AlignmentIndex
)
```

```

System.bool AddPipingFitting( 
   System.String^ PathName,
   System.String^ ConfigName,
   System.short AlignmentIndex
) 
```

#### Parameters

*PathName*
:   Full name and directory location of part file used for this fitting

*ConfigName*
:   Configuration within the fitting part file which should be used

*AlignmentIndex*
:   Each fitting has a varying number of alignment positions; this value allows you to choose the alignment position

#### Return Value

True if successful, false otherwise

Remarks

This method adds a piping fitting to the selected sketch point. The sketch must be the active sketch of the piping assembly.

The alignmentIndex argument controls the alignment of the fitting. For example, you can align a t-piece in two ways: passing 0 aligns the t-piece one way, and passing 1 aligns it the other way.

If the routing DLL is not available, then COM returns ITF\_E\_ROUTINGNOTLOADED.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::AddPipePenetration Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddPipePenetration.md)
