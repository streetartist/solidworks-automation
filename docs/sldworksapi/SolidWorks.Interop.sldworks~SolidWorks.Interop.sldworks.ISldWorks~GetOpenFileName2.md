# GetOpenFileName2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenFileName2`

Prompts the user for the name of the file to open.
Prompts the user for the name of the file to open.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetOpenFileName2( _
   ByVal DialogTitle As System.String, _
   ByVal InitialFileName As System.String, _
   ByVal FileFilter As System.String, _
   ByRef OpenOptions As System.Integer, _
   ByRef ConfigName As System.String, _
   ByRef DisplayName As System.String, _
   ByRef DisplayStateName As System.String _
) As System.String
```

```

Dim instance As ISldWorks
Dim DialogTitle As System.String
Dim InitialFileName As System.String
Dim FileFilter As System.String
Dim OpenOptions As System.Integer
Dim ConfigName As System.String
Dim DisplayName As System.String
Dim DisplayStateName As System.String
Dim value As System.String
 
value = instance.GetOpenFileName2(DialogTitle, InitialFileName, FileFilter, OpenOptions, ConfigName, DisplayName, DisplayStateName)
```

```

System.string GetOpenFileName2( 
   System.string DialogTitle,
   System.string InitialFileName,
   System.string FileFilter,
   out System.int OpenOptions,
   out System.string ConfigName,
   out System.string DisplayName,
   out System.string DisplayStateName
)
```

```

System.String^ GetOpenFileName2( 
   System.String^ DialogTitle,
   System.String^ InitialFileName,
   System.String^ FileFilter,
   [Out] System.int OpenOptions,
   [Out] System.String^ ConfigName,
   [Out] System.String^ DisplayName,
   [Out] System.String^ DisplayStateName
) 
```

#### Parameters

*DialogTitle*
:   Title of the dialog

*InitialFileName*
:   Path and file name of the file to open

*FileFilter*
:   File name extension of the file to open

*OpenOptions*
:   Open options as defined by [swGetOpenFileNameOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGetOpenFileNameOptions_e.html)

*ConfigName*
:   Name of configuration of InitialFileName; comma-separated list of sheet names beginning with active sheet if OpenOptions is swGetOpenFileNameOptions\_e.swGetOpenFileNameOptions\_SelectedSheets

*DisplayName*
:   Recommended name to use for opened file

*DisplayStateName*
:   Selected display state name

#### Return Value

Path and file name of the file to open

Example

[Open File (VBA)](Open_File_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
