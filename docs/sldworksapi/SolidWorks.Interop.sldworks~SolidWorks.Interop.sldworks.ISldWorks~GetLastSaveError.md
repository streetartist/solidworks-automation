# GetLastSaveError Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetLastSaveError`

Gets the last save error issued by Microsoft in the current session.
Gets the last save error issued by Microsoft in the current session.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLastSaveError( _
   ByRef FilePath As System.Object, _
   ByRef ErrorCode As System.Object _
) As System.Object
```

```

Dim instance As ISldWorks
Dim FilePath As System.Object
Dim ErrorCode As System.Object
Dim value As System.Object
 
value = instance.GetLastSaveError(FilePath, ErrorCode)
```

```

System.object GetLastSaveError( 
   out System.object FilePath,
   out System.object ErrorCode
)
```

```

System.Object^ GetLastSaveError( 
   [Out] System.Object^ FilePath,
   [Out] System.Object^ ErrorCode
) 
```

#### Parameters

*FilePath*
:   Path name of the document causing the save error

*ErrorCode*
:   :   Error code of the save

#### Return Value

Text message of the save error

Example

[Get Last Save Error (VBA)](Get_Last_Save_Error_Example_VB.htm)  
[Get Last Save Error (VB.NET)](Get_Last_Save_Error_Example_VBNET.htm)  
[Get Last Save Error (C#)](Get_Last_Save_Error_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetErrorMessages Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetErrorMessages.md)
