# GetLargeDesignReviewState Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetLargeDesignReviewState`

Gets the Large Design Review state of this assembly.
Gets the Large Design Review state of this assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLargeDesignReviewState() As System.Integer
```

```

Dim instance As IAssemblyDoc
Dim value As System.Integer
 
value = instance.GetLargeDesignReviewState()
```

```

System.int GetLargeDesignReviewState()
```

```

System.int GetLargeDesignReviewState(); 
```

#### Return Value

Large Design Review state as defined by [swLargeDesignReviewState\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swLargeDesignReviewState_e.html)

Example

'VBA

'Open an assembly and run the macro.

'==========================================================

Dim swApp As SldWorks.SldWorks

Dim swAssemDoc As SldWorks.AssemblyDoc

Dim boolstatus As Boolean

Dim longstatus As Long, longwarnings As Long

Dim LDRState As Long

Option Explicit

Sub main()

    Set swApp = Application.SldWorks

    Set swAssemDoc = swApp.**ActiveDoc**

    LDRState = swAssemDoc.**GetLargeDesignReviewState**

        If (LDRState = 0) Then

            Debug.Print "LDR State : None"

        ElseIf (LDRState = 1) Then

            Debug.Print "LDR State : LDR Mode"

        Else

             Debug.Print "LDR State : LDR with Assembly Edit Mode"

        End If

     

End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)
