# IsVirtualComponent3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsVirtualComponent3`

Gets the paths to parent assembly components, up to and including the first non-virtual parent, if the model is a virtual component.
Gets the paths to parent assembly components, up to and including the first non-virtual parent, if the model is a virtual component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsVirtualComponent3( _
   ByRef PathChain As System.Object, _
   ByRef TitleChain As System.Object _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim PathChain As System.Object
Dim TitleChain As System.Object
Dim value As System.Boolean
 
value = instance.IsVirtualComponent3(PathChain, TitleChain)
```

```

System.bool IsVirtualComponent3( 
   out System.object PathChain,
   out System.object TitleChain
)
```

```

System.bool IsVirtualComponent3( 
   [Out] System.Object^ PathChain,
   [Out] System.Object^ TitleChain
) 
```

#### Parameters

*PathChain*
:   Array of fully qualified paths to parent assembly components, up to and including the first non-virtual parent assembly component, if the model is a virtual component

*TitleChain*
:   Array of document titles; each document title corresponds to a fully qualified path in PathChain

#### Return Value

True if the component is virtual, false if not

Example

[Get Paths and Titles of Parent of Virtual Component (C#)](Get_Paths_and_Titles_of_Parents_of_Virtual_Component_Example_CSharp.htm)  
[Get Paths and Titles of Parent of Virutal Component (VB.NET)](Get_Paths_and_Titles_of_Parents_of_Virtual_Component_Example_VBNET.htm)  
[Get Paths and Titles of Parent of Virtual Component (VBA)](Get_Paths_and_Titles_of_Parents_of_Virtual_Component_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IComponent2::IsVirtual Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsVirtual.md)  
[IAssemblyDoc::InsertNewVirtualAssembly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertNewVirtualAssembly.md)  
[IComponent2::MakeVirtual Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~MakeVirtual.md)
