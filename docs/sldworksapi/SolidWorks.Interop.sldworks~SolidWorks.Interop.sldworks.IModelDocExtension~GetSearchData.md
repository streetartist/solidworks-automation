# GetSearchData Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSearchData`

Gets the SOLIDWORKS Search, third-party, application keywords from the model document.
Gets the SOLIDWORKS Search, third-party, application keywords from the model document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSearchData( _
   ByVal AppName As System.String, _
   ByRef AppNames As System.Object, _
   ByRef NodeNames As System.Object, _
   ByRef NodeValues As System.Object _
) As System.Integer
```

```

Dim instance As IModelDocExtension
Dim AppName As System.String
Dim AppNames As System.Object
Dim NodeNames As System.Object
Dim NodeValues As System.Object
Dim value As System.Integer
 
value = instance.GetSearchData(AppName, AppNames, NodeNames, NodeValues)
```

```

System.int GetSearchData( 
   System.string AppName,
   out System.object AppNames,
   out System.object NodeNames,
   out System.object NodeValues
)
```

```

System.int GetSearchData( 
   System.String^ AppName,
   [Out] System.Object^ AppNames,
   [Out] System.Object^ NodeNames,
   [Out] System.Object^ NodeValues
) 
```

#### Parameters

*AppName*
:   Third-party application name whose keywords to get

*AppNames*
:   Array of strings of the third-party application name

*NodeNames*
:   Array of strings of the third-party application name's keywords

*NodeValues*
:   Array of strings of the third-party application name's keyword values

#### Return Value

Number of third-party application name's keywords

Example

[Get SOLIDWORKS Search Third-party Keywords (VBA)](Get_SOLIDWORKS_Search_Third-party_Keywords_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::IGetSearchData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetSearchData.md)  
[IModelDocExtension::AddOrUpdateSearchData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddOrUpdateSearchData.md)  
[IModelDocExtension::DeleteSearchData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSearchData.md)  
[IModelDocExtension::GetSearchDataCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSearchDataCount.md)
