# ImportHoleWizardItem Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ImportHoleWizardItem`

Imports data for the specified Hole Wizard standard.
Imports data for the specified Hole Wizard standard.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ImportHoleWizardItem( _
   ByVal StdToImport As System.String, _
   ByVal DestinationFilePath As System.String, _
   ByVal ReplaceData As System.Boolean, _
   ByVal ErrorFile As System.Boolean _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim StdToImport As System.String
Dim DestinationFilePath As System.String
Dim ReplaceData As System.Boolean
Dim ErrorFile As System.Boolean
Dim value As System.Integer
 
value = instance.ImportHoleWizardItem(StdToImport, DestinationFilePath, ReplaceData, ErrorFile)
```

```

System.int ImportHoleWizardItem( 
   System.string StdToImport,
   System.string DestinationFilePath,
   System.bool ReplaceData,
   System.bool ErrorFile
)
```

```

System.int ImportHoleWizardItem( 
   System.String^ StdToImport,
   System.String^ DestinationFilePath,
   System.bool ReplaceData,
   System.bool ErrorFile
) 
```

#### Parameters

*StdToImport*
:   Standard to import (see **Remarks**)

*DestinationFilePath*
:   Path and name of file to import (see **Remarks**)

*ReplaceData*
:   True to replace data, false to not

*ErrorFile*
:   True to create an error file, false to not

#### Return Value

0 if the Hole Wizard standard imported successfully, 1 if not

Remarks

Specify StdToImport with the path and file name as shown on the Hole Wizard tab of the Toolbox, e.g., "**ansi inch\Counterbore Holes\Hex Bolt**".

Specify DestinationFilePath with the path and file name of the Excel Workbook (**\*.xslx**) you want to import. The Excel file name is formatted as follows:

> *standard***\_***hole class***\_***hole type***.xslx**

Example

```

'VBA Preconditions'
```

```

'Open a part.
```

```

'Ensure the *.xlsx file exists.
```

```

Dim swApp As SldWorks.SldWorks  
Dim SourceHWItem As String  
Dim DestinationFoldeName As String  
Dim longstatus As Long
```

```

Option Explicit
```

```

Sub Main()
```

```

    Set swApp = Application.SldWorks  
     
    SourceHWItem = "ansi inch\Counterbore Holes\Hex Bolt"  
     
    DestinationFolderName = "C:\temp\ANSI Inch_Counterbore Holes_Hex Bolt.xlsx"  
     
    longstatus = swApp.ImportHoleWizardItem(SourceHWItem, DestinationFolderName, True, True)  
     
             
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
[ISldWorks::ExportHoleWizardItem Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ExportHoleWizardItem.md)
