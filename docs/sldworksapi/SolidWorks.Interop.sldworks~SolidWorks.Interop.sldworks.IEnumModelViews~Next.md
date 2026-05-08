# Next Method (IEnumModelViews)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumModelViews~Next`

Gets the next model view in the model views enumeration.
Gets the next model view in the model views enumeration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As ModelView, _
   ByRef PceltFetched As System.Integer _
) 
```

```

Dim instance As IEnumModelViews
Dim Celt As System.Integer
Dim Rgelt As ModelView
Dim PceltFetched As System.Integer
 
instance.Next(Celt, Rgelt, PceltFetched)
```

```

void Next( 
   System.int Celt,
   out ModelView Rgelt,
   out System.int PceltFetched
)
```

```

void Next( 
   System.int Celt,
   [Out] ModelView^ Rgelt,
   [Out] System.int PceltFetched
) 
```

#### Parameters

*Celt*
:   Number of model views for the model views enumeration

*Rgelt*
:   Pointer to an array of [model views](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md) of size Celt

*PceltFetched*
:   Pointer to the number of model views returned from the list; this value can be less than celt if you ask for more model views than exist, or it can be NULL if no more model views exist

Remarks

For use in in-process DLLs only.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnumModelViews Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumModelViews.md)  
[IEnumModelViews Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumModelViews_members.md)
