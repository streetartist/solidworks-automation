# ImportToolboxItem Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ImportToolboxItem`

Imports data for the specified Toolbox standard.
Imports data for the specified Toolbox standard.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ImportToolboxItem( _
   ByVal StdToImport As System.String, _
   ByVal DestinationFilePath As System.String _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim StdToImport As System.String
Dim DestinationFilePath As System.String
Dim value As System.Integer
 
value = instance.ImportToolboxItem(StdToImport, DestinationFilePath)
```

```

System.int ImportToolboxItem( 
   System.string StdToImport,
   System.string DestinationFilePath
)
```

```

System.int ImportToolboxItem( 
   System.String^ StdToImport,
   System.String^ DestinationFilePath
) 
```

#### Parameters

*StdToImport*
:   Standard to import (see **Remarks**)

*DestinationFilePath*
:   Path and name of file to import (see **Remarks**)

#### Return Value

0 if the Toolbox standard imported successfully, 1 if not

Remarks

Specify StdToImport with the path and file name beneath **C:\SOLIDWORKS Data\browser**, e.g., "**ansi inch\bolts and screws\hex head\heavy hex bolt\_ai.sldprt**".

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
Option Explicit
```

```

Sub Main()
```

```

    Set swApp = Application.SldWorks  
     
    SourceHWItem = "ansi inch\bolts and screws\hex head\heavy hex bolt_ai.sldprt"  
     
    DestinationFolderName = "C:\temp\AI_Heavy Hex Bolt.xlsx"  
     
    longstatus = swApp.ImportToolboxItem(SourceHWItem, DestinationFolderName)  
     
             
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
[ISldWorks::ExportToolboxItem Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ExportToolboxItem.md)
