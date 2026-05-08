# ExportHoleWizardItem Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ExportHoleWizardItem`

Exports data for the specified Hole Wizard standard.
Exports data for the specified Hole Wizard standard.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ExportHoleWizardItem( _
   ByVal StdToExport As System.String, _
   ByVal DestinationFolderPath As System.String _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim StdToExport As System.String
Dim DestinationFolderPath As System.String
Dim value As System.Integer
 
value = instance.ExportHoleWizardItem(StdToExport, DestinationFolderPath)
```

```

System.int ExportHoleWizardItem( 
   System.string StdToExport,
   System.string DestinationFolderPath
)
```

```

System.int ExportHoleWizardItem( 
   System.String^ StdToExport,
   System.String^ DestinationFolderPath
) 
```

#### Parameters

*StdToExport*
:   Standard to export (see **Remarks**)

*DestinationFolderPath*
:   Path where to export the data (see **Remarks**)

#### Return Value

0 if successful, 1 if errors

Remarks

Specify StdToImport with the path and file name as shown on the Hole Wizard tab of the Toolbox, e.g., "**ansi inch\Counterbore Holes\Hex Bolt**".

Specify DestinationFolderPath with the path where to create the Excel Workbook (**\*.xslx**). The data is exported to a file whose name is formatted as follows:

> *standard***\_***hole class***\_***hole type***.xslx**

Example

```

'VBA Preconditions'
```

```

'Open a part.
```

```

'Ensure that c:\temp exists.
```

```

Dim swApp As SldWorks.SldWorks  
Dim SourceHWItem As String  
Dim DestinationFoldeName As String  
Dim longstatus As Long  
Option Explicit
```

```

Sub Main()
```

```

    Set swApp = Application.SldWorks  
     
    SourceHWItem = "ansi inch\Counterbore Holes\Hex Bolt"  
     
    DestinationFolderName = "C:\temp"  
     
    longstatus = swApp.ExportHoleWizardItem(SourceHWItem, DestinationFolderName)  
     
    Exit Sub  
       
```

```

End Sub  

```

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::ImportHoleWizardItem Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ImportHoleWizardItem.md)
