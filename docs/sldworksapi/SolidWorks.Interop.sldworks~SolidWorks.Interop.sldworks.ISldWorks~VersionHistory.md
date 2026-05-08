# VersionHistory Method (ISldWorks)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~VersionHistory`

Gets a list of strings indicating the versions in which a model was saved.
Gets a list of strings indicating the versions in which a model was saved.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function VersionHistory( _
   ByVal FileName As System.String _
) As System.Object
```

```

Dim instance As ISldWorks
Dim FileName As System.String
Dim value As System.Object
 
value = instance.VersionHistory(FileName)
```

```

System.object VersionHistory( 
   System.string FileName
)
```

```

System.Object^ VersionHistory( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   Full path name of the model for which to get the version history

#### Return Value

Array of strings containing the version history

Remarks

This information is retrieved from the file on disk, not from the open document.

There is one array entry for each major release of the SOLIDWORKS software in which the document has been saved. The format for each entry is a major release code followed by one or more minor release codes separated by commas:

 <major release code>[<minor release code>]  
  
- or -

 <major release code>[<minor release code>,<minor release code>...]

where <major release code> equals a number that remains constant through a major release of the SOLIDWORKS software. For example, the following values are returned based on the corresponding major SOLIDWORKS version:

|  |  |
| --- | --- |
| **SOLIDWORKS Release** | **Version Number** |
| SOLIDWORKS 95 | 44 |
| SOLIDWORKS 96 | 243 |
| SOLIDWORKS 97 | 483 |
| SOLIDWORKS 97Plus | 629 |
| SOLIDWORKS 98 | 822 |
| SOLIDWORKS 98Plus | 1008 |
| SOLIDWORKS 99 | 1137 |
| SOLIDWORKS 2000 | 1500 |
| SOLIDWORKS 2001 | 1750 |
| SOLIDWORKS 2001Plus | 1950 |
| SOLIDWORKS 2003 | 2200 |
| SOLIDWORKS 2004 | 2500 |
| SOLIDWORKS 2005 | 2800 |
| SOLIDWORKS 2006 | 3100 |
| SOLIDWORKS 2007 | 3400 |
| SOLIDWORKS 2008 | 3800 |
| SOLIDWORKS 2009 | 4100 |
| SOLIDWORKS 2010 | 4400 |
| SOLIDWORKS 2011 | 4700 |
| SOLIDWORKS 2012 | 5000 |
| SOLIDWORKS 2013 | 6000 |
| SOLIDWORKS 2014 | 7000 |
| SOLIDWORKS 2015 | 8000 |
| SOLIDWORKS 2016 | 9000 |
| SOLIDWORKS 2017 | 10000 |
| SOLIDWORKS 2018 | 11000 |
| SOLIDWORKS 2019 | 12000 |
| SOLIDWORKS 2020 | 13000 |
| SOLIDWORKS 2021 | 14000 |
| SOLIDWORKS 2022 | 15000 |
| SOLIDWORKS 2023 | 16000 |
| SOLIDWORKS 2024 | 17000 |
| SOLIDWORKS 2025 | 18000 |

The <minor release code> equals the year and day of manufacture of a saving version (for example, 1997/320).

To get the version history of a document that is currently open, use [IModelDoc2::VersionHistory](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~VersionHistory.md).

Example

[Get Version History (VBA)](Get_Version_History_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::IVersionHistory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IVersionHistory.md)  
[ISldWorks::RevisionNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RevisionNumber.md)  
[ISldWorks::GetBuildNumbers2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetBuildNumbers2.md)  
[IModelDocExtension::IsFutureVersion Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsFutureVersion.md)
