# Get4 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Get4`

Obsolete. Superseded by ICustomPropertyManager::Get5.
Obsolete. Superseded by [ICustomPropertyManager::Get5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Get5.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Get4( _
   ByVal FieldName As System.String, _
   ByVal UseCached As System.Boolean, _
   ByRef ValOut As System.String, _
   ByRef ResolvedValOut As System.String _
) As System.Boolean
```

```

Dim instance As ICustomPropertyManager
Dim FieldName As System.String
Dim UseCached As System.Boolean
Dim ValOut As System.String
Dim ResolvedValOut As System.String
Dim value As System.Boolean
 
value = instance.Get4(FieldName, UseCached, ValOut, ResolvedValOut)
```

```

System.bool Get4( 
   System.string FieldName,
   System.bool UseCached,
   out System.string ValOut,
   out System.string ResolvedValOut
)
```

```

System.bool Get4( 
   System.String^ FieldName,
   System.bool UseCached,
   [Out] System.String^ ValOut,
   [Out] System.String^ ResolvedValOut
) 
```

#### Parameters

*FieldName*
:   Name of the custom property

*UseCached*
:   True if the configuration has been activated, false if not (see Remarks)

*ValOut*
:   Value of the custom property

*ResolvedValOut*
:   Evaluated value of the custom property

#### Return Value

True if up-to-date data is returned, false if not (see Remarks)

Remarks

This method can get the cached custom property, even if the configuration is not currently active, without having to change configurations.

|  |  |  |
| --- | --- | --- |
| If UseCached is set to... | And the configuration has already been activated... | Then... |
| True | Yes | - Up-to-date data is returned and return value = true |
| True | No | - Cached data is returned and return value = false |
| False | Yes | - Up-to-date data is returned and return value = true |
| False | No | - Up-to-date data is returned and return value = true |

This method returns configuration-specific, linked, custom-property, evaluated data more quickly than the now obsolete [ICustomPropertyManager::Get2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Get2.md), if the configuration was previously activated.

If you always want up-to-date data, then you should set UseCached to false. This might result in a more time-consuming call if the configuration was not previously activated.

This method does not preface the resolved evaluated values of external referenced documents with **fromparent+**, unlike the now obsolete [ICustomPropertyManager::Get3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Get3.md).

Example

[Get Custom Properties of Referenced Part (C#)](Get_Custom_Properties_of_Referenced_Part_Example_CSharp.htm)  
[Get Custom Properties of Referenced Part (VB.NET)](Get_Custom_Properties_of_Referenced_Part_Example_VBNET.htm)  
[Get Custom Properties of Referenced Part (VBA)](Get_Custom_Properties_of_Referenced_Part_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.md)  
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.md)
