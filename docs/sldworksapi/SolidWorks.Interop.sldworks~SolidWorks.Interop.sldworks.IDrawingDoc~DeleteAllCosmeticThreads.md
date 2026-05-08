# DeleteAllCosmeticThreads Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~DeleteAllCosmeticThreads`

Deletes all cosmetic threads, which do not have callouts, in a drawing of an assembly only.
Deletes all cosmetic threads, which do not have callouts, in a drawing of an assembly only.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub DeleteAllCosmeticThreads() 
```

```

Dim instance As IDrawingDoc
 
instance.DeleteAllCosmeticThreads()
```

```

void DeleteAllCosmeticThreads()
```

```

void DeleteAllCosmeticThreads(); 
```

Remarks

This method only deletes cosmetic threads in a drawing of an assembly; this method does not delete cosmetic threads in a drawing of a part.

By default, cosmetic threads are not imported into an drawing of an assembly for performance reasons, but are imported into a drawing of part and belong to the features in the part; thus, they cannot be deleted using this method.

This method also does not delete any cosmetic threads with callouts in a drawing of an assembly.

Example

**VB.NET:**

'---------------------------------------------------

'

' Preconditions: Drawing of an assembly with

' cosmetic threads is active.

'

' Postconditions: Cosmetic threads without callouts

' are deleted.

'

'---------------------------------------------------

Option Explicit On

 

Imports SOLIDWORKS.Interop.sldworks

Imports SOLIDWORKS.Interop.swconst

Imports System

Partial Class SOLIDWORKSMacro

> Public Sub main()
>
> > Dim swDrawingDoc As DrawingDoc
> >
> > Dim swModel As ModelDoc2
> >
> > Dim boolstatus As Boolean
> >
> >  
> >
> > swDrawingDoc = swApp.ActiveDoc
> >
> > swDrawingDoc.DeleteAllCosmeticThreads()
> >
> > swModel = swDrawingDoc
> >
> > boolstatus = swModel.ForceRebuild3(False)
>
> End Sub
>
>  
>
> ''' <summary>
>
> ''' The SldWorks swApp variable is pre-assigned for you.
>
> ''' </summary>
>
> Public swApp As SldWorks

End Class

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[ICThread Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread.md)
