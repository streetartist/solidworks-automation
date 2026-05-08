# IGetSearchData Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetSearchData`

Gets the SOLIDWORKS Search, third-party, application keywords from the model document.
Gets the SOLIDWORKS Search, third-party, application keywords from the model document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IGetSearchData( _
   ByVal AppName As System.String, _
   ByVal Count As System.Integer, _
   ByRef AppNames As System.String, _
   ByRef NodeNames As System.String, _
   ByRef NodeValues As System.String _
) 
```

```

Dim instance As IModelDocExtension
Dim AppName As System.String
Dim Count As System.Integer
Dim AppNames As System.String
Dim NodeNames As System.String
Dim NodeValues As System.String
 
instance.IGetSearchData(AppName, Count, AppNames, NodeNames, NodeValues)
```

```

void IGetSearchData( 
   System.string AppName,
   System.int Count,
   out System.string AppNames,
   out System.string NodeNames,
   out System.string NodeValues
)
```

```

void IGetSearchData( 
   System.String^ AppName,
   System.int Count,
   [Out] System.String^ AppNames,
   [Out] System.String^ NodeNames,
   [Out] System.String^ NodeValues
) 
```

#### Parameters

*AppName*
:   Third-party application name whose keywords to get

*Count*
:   Number of third-party application keywords

*AppNames*
:   - in-process, unmanaged C++: Pointer to an array of the third-party application names

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*NodeNames*
:   - in-process, unmanaged C++: Pointer to an array of the third-party application name's keywords

    - VBA, VB.NET, C#, and C++/CLI: Not supported

*NodeValues*
:   - in-process, unmanaged C++: Pointer to an array of the third-party application name's keyword values

    - VBA, VB.NET, C#, and C++/CLI: Not supported

#### Return Value

Number of third-party application name's keywords

Remarks

Before calling this method, call [IModelDocExtension::GetSearchDataCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSearchDataCount.md) to get the value of Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::AddOrUpdateSearchData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddOrUpdateSearchData.md)  
[IModelDocExtension::DeleteSearchData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSearchData.md)  
[IModelDocExtension::GetSearchData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSearchData.md)
