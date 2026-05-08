# GetCurrentFileUser Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentFileUser`

Gets the name of the user who has the the specified document open.
Gets the name of the user who has the the specified document open.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCurrentFileUser( _
   ByVal FilePathName As System.String _
) As System.String
```

```

Dim instance As ISldWorks
Dim FilePathName As System.String
Dim value As System.String
 
value = instance.GetCurrentFileUser(FilePathName)
```

```

System.string GetCurrentFileUser( 
   System.string FilePathName
)
```

```

System.String^ GetCurrentFileUser( 
   System.String^ FilePathName
) 
```

#### Parameters

*FilePathName*
:   Full path and filename of the document

Example

**Visual Basic for Applications (VBA)**

**'-----------------------------------**

Option Explicit

Dim swApp As SldWorks.SldWorks

Sub main()

Set swApp = Application.SldWorks

' Substitute your path and filename

Debug.Print swApp.GetCurrentFileUser("C:\temp\b&r.sldprt")

End Sub

**'-----------------------------------**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
