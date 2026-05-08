# RunAttachedMacro Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunAttachedMacro`

Runs the specified attached macro, module, and procedure.
Runs the specified attached macro, module, and procedure.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RunAttachedMacro( _
   ByVal FileName As System.String, _
   ByVal ModuleName As System.String, _
   ByVal ProcedureName As System.String _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim FileName As System.String
Dim ModuleName As System.String
Dim ProcedureName As System.String
Dim value As System.Boolean
 
value = instance.RunAttachedMacro(FileName, ModuleName, ProcedureName)
```

```

System.bool RunAttachedMacro( 
   System.string FileName,
   System.string ModuleName,
   System.string ProcedureName
)
```

```

System.bool RunAttachedMacro( 
   System.String^ FileName,
   System.String^ ModuleName,
   System.String^ ProcedureName
) 
```

#### Parameters

*FileName*
:   Filename of macro to run (do not include a path)

*ModuleName*
:   Module of specified macro to run

*ProcedureName*
:   Procedure of specified macro to run

#### Return Value

True if macro runs, false if not

Remarks

An example of an attached macro is a macro that is attached to the active document's Design Binder.

Example

**Visual Basic for Applications (VBA)**

Create two VBA macros using the following code samples. Attach **RunMacroSub.swp** to the active document's Design Binder. Then run **RunAttachedMacro.swp**.

'--------------------------------------  
' RunAttachedMacro.swp  
'-------------------------------------  
Option Explicit  
Dim swApp As SldWorks.SldWorks  
Dim boolstatus As Boolean

Sub main()  
   Set swApp = Application.SldWorks  
   Dim RunMacroError As Long  
   boolstatus = swApp.**RunAttachedMacro**("RunMacroSub.swp", "RunMacroSub1", "main")  
End Sub

'---------------------------------------  
' RunMacroSub.swp'  
'---------------------------------------  
Option Explicit  
Dim swApp As SldWorks.SldWorks

Sub alternate()  
   Set swApp = Application.SldWorks  
   swApp.SendMsgToUser "RunMacroSub1:alternate() called."  
End Sub

Sub main()  
   Set swApp = Application.SldWorks  
   swApp.SendMsgToUser "RunMacroSub1:main() called."

End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::RunMacro2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunMacro2.md)
