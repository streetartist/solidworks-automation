# GetItemsNameAndPath Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~GetItemsNameAndPath`

Gets all reference components' names and paths.
Gets all reference components' names and paths.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetItemsNameAndPath( _
   ByRef IdsList As System.Object, _
   ByRef NamesList As System.Object, _
   ByRef PathsList As System.Object _
) 
```

```

Dim instance As IAdvancedSaveAsOptions
Dim IdsList As System.Object
Dim NamesList As System.Object
Dim PathsList As System.Object
 
instance.GetItemsNameAndPath(IdsList, NamesList, PathsList)
```

```

void GetItemsNameAndPath( 
   out System.object IdsList,
   out System.object NamesList,
   out System.object PathsList
)
```

```

void GetItemsNameAndPath( 
   [Out] System.Object^ IdsList,
   [Out] System.Object^ NamesList,
   [Out] System.Object^ PathsList
) 
```

#### Parameters

*IdsList*
:   Array of component reference IDs

*NamesList*
:   Array of component reference names

*PathsList*
:   Array of component reference paths

Remarks

IdsList, NamesList, and PathsList are the same array size and map one to one. Call this method to obtain the current list of component references before calling [IAdvancedSaveAsOptions::ModifyItemsNameAndPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~ModifyItemsNameAndPath.md) to modify them.

This method lists component references according to the Options parameter that was specified in the call to [IModelDocExtension::GetAdvancedSaveAsOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAdvancedSaveAsOptions.md).

Example

See the [IAdvancedSaveAsOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAdvancedSaveAsOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.md)  
[IAdvancedSaveAsOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions_members.md)
