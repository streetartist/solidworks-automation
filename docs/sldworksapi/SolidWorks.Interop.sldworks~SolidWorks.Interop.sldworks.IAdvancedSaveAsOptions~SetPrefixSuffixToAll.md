# SetPrefixSuffixToAll Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~SetPrefixSuffixToAll`

Sets a prefix and/or a suffix on all component reference names.
Sets a prefix and/or a suffix on all component reference names.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetPrefixSuffixToAll( _
   ByVal PrefixString As System.String, _
   ByVal SuffixString As System.String _
) 
```

```

Dim instance As IAdvancedSaveAsOptions
Dim PrefixString As System.String
Dim SuffixString As System.String
 
instance.SetPrefixSuffixToAll(PrefixString, SuffixString)
```

```

void SetPrefixSuffixToAll( 
   System.string PrefixString,
   System.string SuffixString
)
```

```

void SetPrefixSuffixToAll( 
   System.String^ PrefixString,
   System.String^ SuffixString
) 
```

#### Parameters

*PrefixString*
:   Prefix

*SuffixString*
:   Suffix

Remarks

This method applies a prefix/suffix to the names of all references except the top-level document. After calling this method, call [IAdvancedSaveAsOptions::ModifyItemsNameAndPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~ModifyItemsNameAndPath.md) to modify the name and path of individual references and/or the top-level assembly.

Example

See the [IAdvancedSaveAsOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAdvancedSaveAsOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.md)  
[IAdvancedSaveAsOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions_members.md)
