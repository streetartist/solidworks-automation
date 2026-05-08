# NeedErrorList Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~NeedErrorList`

Gets or sets the need error list option.
Gets or sets the need error list option.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property NeedErrorList As System.Boolean
```

```

Dim instance As ITessellation
Dim value As System.Boolean
 
instance.NeedErrorList = value
 
value = instance.NeedErrorList
```

```

System.bool NeedErrorList {get; set;}
```

```

property System.bool NeedErrorList {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True generates need error list option, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)  
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.md)  
[ITessellate::GetErrorList Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetErrorList.md)  
[ITessellate::IGetErrorList2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetErrorList2.md)  
[ITessellate::IGetErrorListCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetErrorListCount.md)
