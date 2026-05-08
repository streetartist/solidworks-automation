# IGetVersionHistoryCount Method (ISldWorks)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetVersionHistoryCount`

Gets the size of the array required to hold data returned by ISldWorks::IVersionHistory.
Gets the size of the array required to hold data returned by [ISldWorks::IVersionHistory](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IVersionHistory.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetVersionHistoryCount( _
   ByVal FileName As System.String _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim FileName As System.String
Dim value As System.Integer
 
value = instance.IGetVersionHistoryCount(FileName)
```

```

System.int IGetVersionHistoryCount( 
   System.string FileName
)
```

```

System.int IGetVersionHistoryCount( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   Full pathname of the model for which to get the version history

#### Return Value

Size of array required for [ISldWorks::IVersionHistory](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IVersionHistory.md)

Remarks

If the file is not found or an error occurs, then this method returns 0.

To get the version history of a document that is currently open, use [IModelDoc2::VersionHistory](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~VersionHistory.md) or [IModelDoc2::IVersionHistory](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IVersionHistory.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::VersionHistory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~VersionHistory.md)
